"""
Instead of using bach config filees, we will just separate them into different files we can just import

This is config `alpha.py`:
Just to try to get the first run running.
"""

import argparse
import os
import sys


def get_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()

    # For data processing
    path_to_running_file = os.path.abspath(sys.argv[0])
    default_cache_dir = os.path.join(os.path.dirname(path_to_running_file), ".cache")
    ap.add_argument(
        "--QAtriplets_raw_dir",
        type=str,
        default=os.path.join(path_to_running_file, "data/itl/multihop_ds_datasets_FbWiki_TriviaQA.csv"),
    )
    ap.add_argument(
        "--QAtriplets_cache_dir",
        type=str,
        default=os.path.join(default_cache_dir, "qa_triplets.csv"),
    )
    ap.add_argument("--gpu", type=int, default=0)
    ap.add_argument("--seed", type=int, default=420, metavar="S")
    ap.add_argument("--tokenizer", type=str, default="bert-base-uncased")

    # NOTE: Legacy Parameters
    # Might want to get rid of them as we see fit.
    ap.add_argument("--relation_only", type=str, default="", help="")
    ap.add_argument("--history_dim", type=str, default="", help="")
    ap.add_argument("--history_num_layers", type=str, default="", help="")
    ap.add_argument("--entity_dim", type=str, default="", help="")
    ap.add_argument("--relation_dim", type=str, default="", help="")
    ap.add_argument("--ff_dropout_rate", type=str, default="", help="")
    ap.add_argument("--xavier_initialization", type=str, default="", help="")
    ap.add_argument("--relation_only_in_path", type=str, default="", help="")
        
    ap.add_argument('--run_analysis', action='store_true',
                    help='run algorithm analysis and print intermediate results (default: False)')
    ap.add_argument('--data_dir', type=str, default=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'),
                    help='directory where the knowledge graph data is stored (default: None)')
    ap.add_argument('--model_root_dir', type=str, default=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model'),
                    help='root directory where the model parameters are stored (default: None)')
    ap.add_argument('--model_dir', type=str, default=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model'),
                    help='directory where the model parameters are stored (default: None)')
    ap.add_argument('--model', type=str, default='point',
                    help='knowledge graph QA model (default: point)')
    ap.add_argument('--use_action_space_bucketing', action='store_true',
                    help='bucket adjacency list by outgoing degree to avoid memory blow-up (default: False)')
    ap.add_argument('--train_entire_graph', type=bool, default=False,
                    help='add all edges in the graph to extend training set (default: False)')
    ap.add_argument('--num_epochs', type=int, default=200,
                    help='maximum number of pass over the entire training set (default: 20)')
    ap.add_argument('--num_wait_epochs', type=int, default=5,
                    help='number of epochs to wait before stopping training if dev set performance drops')
    ap.add_argument('--num_peek_epochs', type=int, default=2,
                    help='number of epochs to wait for next dev set result check (default: 2)')
    ap.add_argument('--start_epoch', type=int, default=0,
                    help='epoch from which the training should start (default: 0)')
    ap.add_argument('--batch_size', type=int, default=256,
                    help='mini-batch size (default: 256)')
    ap.add_argument('--train_batch_size', type=int, default=256,
                    help='mini-batch size during training (default: 256)')
    ap.add_argument('--dev_batch_size', type=int, default=64,
                    help='mini-batch size during inferece (default: 64)')
    ap.add_argument('--learning_rate', type=float, default=0.0001,
                    help='learning rate (default: 0.0001)')
    ap.add_argument('--learning_rate_decay', type=float, default=1.0,
                    help='learning rate decay factor for the Adam optimizer (default: 1)')
    ap.add_argument('--adam_beta1', type=float, default=0.9,
                    help='Adam: decay rates for the first movement estimate (default: 0.9)')
    ap.add_argument('--adam_beta2', type=float, default=0.999,
                    help='Adam: decay rates for the second raw movement estimate (default: 0.999)')
    ap.add_argument('--grad_norm', type=float, default=10000,
                    help='norm threshold for gradient clipping (default 10000)')
    ap.add_argument('--action_dropout_rate', type=float, default=0.1,
                    help='Dropout rate for randomly masking out knowledge graph edges (default: 0.1)')
    ap.add_argument('--action_dropout_anneal_factor', type=float, default=0.95,
	                help='Decrease the action dropout rate once the dev set results stopped increase (default: 0.95)')
    ap.add_argument('--action_dropout_anneal_interval', type=int, default=1000,
		            help='Number of epochs to wait before decreasing the action dropout rate (default: 1000. Action '
                         'dropout annealing is not used when the value is >= 1000.)')
    ap.add_argument('--num_rollouts', type=int, default=20,
                    help='number of rollouts (default: 20)')
    ap.add_argument('--num_rollout_steps', type=int, default=3,
                    help='maximum path length (default: 3)')
    ap.add_argument('--beta', type=float, default=0.0,
                    help='entropy regularization weight (default: 0.0)')
    ap.add_argument('--gamma', type=float, default=1,
                    help='moving average weight (default: 1)')
    ap.add_argument('--baseline', type=str, default='n/a',
                    help='baseline used by the policy gradient algorithm (default: n/a)')
    ap.add_argument('--beam_size', type=int, default=100,
                    help='size of beam used in beam search inference (default: 100)')


    return ap.parse_args()

