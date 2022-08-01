REGISTRY = {}

from .rnn_agent import RNNAgent
from .ff_agent import FFAgent
from .central_rnn_agent import CentralRNNAgent
from .iqn_rnn_agent import IQNRNNAgent


REGISTRY["rnn"] = RNNAgent
REGISTRY["ff"] = FFAgent
REGISTRY["iqn_rnn"] = IQNRNNAgent
REGISTRY["central_rnn"] = CentralRNNAgent
