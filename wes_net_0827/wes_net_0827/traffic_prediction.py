import os
import time
import h5py
import torch
import numpy as np
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from traffic_dataset import LoadData
from utils import Evaluation
from models.gcnlstm import GCN_LSTM
from models.gcnnet import GCN
from models.gat import GATNet

import warnings
warnings.filterwarnings('ignore')



def main():
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    train_data = LoadData(data_path=["data/test17.csv", "data/test17.npz"], num_nodes=17, divide_days=[583, 146],
                          time_interval=1, history_length=6,
                          train_mode="train")

    train_loader = DataLoader(train_data, batch_size=32, shuffle=True, num_workers=8)

    test_data = LoadData(data_path=["data/test17.csv", "data/test17.npz"], num_nodes=17, divide_days=[583, 146],
                         time_interval=1, history_length=6,
                         train_mode="test")

    test_loader = DataLoader(test_data, batch_size=32, shuffle=False, num_workers=8)

    # my_net = GCN(in_c=6 * 3, hid_c=6, out_c=1)
    my_net = GATNet(in_c=6 * 3, hid_c=6, out_c=1, n_heads=2)
    # my_net = GCN_LSTM(in_c=6 * 3, hid_c=32, out_c=1, o_f=64)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    my_net = my_net.to(device)

    criterion = nn.MSELoss()

    optimizer = optim.Adam(params=my_net.parameters())


    # Train model
    Epoch = 50

    my_net.train()
    for epoch in range(Epoch):
        epoch_loss = 0.0
        count = 0
        start_time = time.time()
        for data in train_loader:
            my_net.zero_grad()
            count +=1
            predict_value = my_net(data, device).to(torch.device("cpu"))

            loss = criterion(predict_value, data["flow_y"])

            epoch_loss += loss.item()

            loss.backward()

            optimizer.step()
        end_time = time.time()

        print("Epoch: {:04d}, Loss: {:02.4f}, Time: {:02.2f} mins".format(epoch, 1000 * epoch_loss / len(train_data),
                                                                          (end_time - start_time) / 60))



    # Test Model
    # MAE, MAPE, RMSE = [], [], []
    my_net.eval()
    with torch.no_grad():
        MAE, MAPE, RMSE = [], [], []
        Target = np.zeros([17, 1, 1])
        Predict = np.zeros_like(Target)

        total_loss = 0.0
        for data in test_loader:
            predict_value = my_net(data, device).to(torch.device("cpu"))

            loss = criterion(predict_value, data["flow_y"])

            total_loss += loss.item()
            predict_value = predict_value.transpose(0, 2).squeeze(0)   # (17,64,1)
            target_value = data["flow_y"].transpose(0, 2).squeeze(0)[:, :, 0][:, :, np.newaxis]

            performance, data_to_save = compute_performance(predict_value, target_value, test_loader)

            # [N, T, D] = [N, T1+T2+..., D]
            Predict = np.concatenate([Predict, data_to_save[0]], axis=1)
            Target = np.concatenate([Target, data_to_save[1]], axis=1)

            MAE.append(performance[0])
            MAPE.append(performance[1])
            RMSE.append(performance[2])

            print("Test Loss: {:02.4f}".format(1000 * total_loss / len(test_data)))

    print("Performance:   {:2.2f} {:2.2f}% {:2.2f}".format(np.mean(MAE), np.mean(MAPE * 100), np.mean(RMSE)))

    Predict = np.delete(Predict, 0, axis=1)
    Target = np.delete(Target, 0, axis=1)

    result_file = "GATLSTM_result.h5"
    file_obj = h5py.File(result_file, "w")

    file_obj["predict"] = Predict  # [N, T, D]
    file_obj["target"] = Target  # [N, T, D]


def compute_performance(prediction, target, data):
    try:
        dataset = data.dataset  # The data is of type dataloader, which is turned into dataset by the attribute .dataset class below it
    except:
        dataset = data  # The data is of dataset type and is assigned directly to the value

    prediction = LoadData.recover_data(dataset.flow_norm[0], dataset.flow_norm[1], prediction.numpy())
    target = LoadData.recover_data(dataset.flow_norm[0], dataset.flow_norm[1], target.numpy())

    mae, mape, rmse = Evaluation.total(target.reshape(-1), prediction.reshape(-1))

    performance = [mae, mape, rmse]
    recovered_data = [prediction[:, :, 0][:, :, np.newaxis], target[:, :, 0][:, :, np.newaxis]]

    return performance, recovered_data


if __name__ == '__main__':
    main()
    # visualize_result(h5_file="GCN_result.h5",
    # nodes_id = 120, time_se = [0, 24 * 12 * 2],
    # visualize_file = "gat_node_120")