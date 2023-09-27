import torch
import torch.nn as nn


class GCN_LSTM(nn.Module):
    def __init__(self, in_c, hid_c, out_c, o_f):
        super(GCN_LSTM, self).__init__()
        self.linear_1 = nn.Linear(in_c, hid_c)
        self.linear_2 = nn.Linear(hid_c, o_f)
        self.act = nn.ReLU()

        self.lstm = nn.LSTM(o_f, 64, batch_first=True, dropout=0.5)
        self.fc = nn.Sequential(
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, out_c)
        )

    def forward(self, data, device):
        graph_data = data["graph"].to(device)[0]
        graph_data = GCN_LSTM.process_graph(graph_data)

        flow_x = data["flow_x"].to(device)

        B, N = flow_x.size(0), flow_x.size(1)

        flow_x = flow_x.view(B, N, -1)

        output_1 = self.linear_1(flow_x)
        output_1 = self.act(torch.matmul(graph_data, output_1))

        output_2 = self.linear_2(output_1)
        output_2 = self.act(torch.matmul(graph_data, output_2))

        output_3, _ = self.lstm(output_2)

        output_4 = self.fc(output_3)

        return output_4.unsqueeze(2)

    @staticmethod
    def process_graph(graph_data):
        N = graph_data.size(0)
        matrix_i = torch.eye(N, dtype=torch.float, device=graph_data.device)
        graph_data += matrix_i

        degree_matrix = torch.sum(graph_data, dim=1, keepdim=False)
        degree_matrix = degree_matrix.pow(-1)
        degree_matrix[degree_matrix == float("inf")] = 0.

        degree_matrix = torch.diag(degree_matrix)

        return torch.mm(degree_matrix, graph_data)