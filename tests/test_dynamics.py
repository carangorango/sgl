import numpy as np
import pytest

from democritus.dynamics import Dynamics, ReplicatorDynamics, BestResponseDynamics, QuantalResponseDynamics


class TestDynamics(object):
    def test_update_sender(self):
        dynamics = Dynamics()
        with pytest.raises(NotImplementedError):
            dynamics.update_sender(None, None, None)

    def test_update_receiver(self):
        dynamics = Dynamics()
        with pytest.raises(NotImplementedError):
            dynamics.update_receiver(None, None, None)


class TestReplicatorDynamics(object):
    def test_update_sender(self, sim_max_game):
        game = sim_max_game
        dynamics = ReplicatorDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0.156, 0.844], [0.742, 0.258]]

    def test_update_receiver(self, sim_max_game):
        game = sim_max_game
        dynamics = ReplicatorDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[0.382, 0.618], [0.968, 0.032]]

    def test_update_sender_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = ReplicatorDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0.273, 0.727], [0.689, 0.311]]

    def test_update_receiver_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = ReplicatorDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[0.620, 0.380], [0.938, 0.062]]


class TestBestResponseDynamics(object):
    def test_update_sender(self, sim_max_game):
        game = sim_max_game
        dynamics = BestResponseDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0, 1], [1, 0]]

    def test_update_receiver(self, sim_max_game):
        game = sim_max_game
        dynamics = BestResponseDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[1, 0], [1, 0]]

    def test_update_sender_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = BestResponseDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0.2, 0.8], [0.909, 0.091]]

    def test_update_receiver_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = BestResponseDynamics()
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[0.952, 0.048], [0.952, 0.048]]


class TestQuantalResponseDynamics(object):
    def test_update_sender(self, sim_max_game):
        game = sim_max_game
        dynamics = QuantalResponseDynamics(5)
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0.005, 0.995], [0.959, 0.041]]

    def test_update_receiver(self, sim_max_game):
        game = sim_max_game
        dynamics = QuantalResponseDynamics(5)
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[0.788, 0.212], [0.967, 0.033]]

    def test_update_sender_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = QuantalResponseDynamics(5)
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_sender_strategy = dynamics.update_sender(sender_strategy, receiver_strategy, game)
        assert np.round(new_sender_strategy, decimals=3).tolist() == [[0.196, 0.804], [0.872, 0.128]]

    def test_update_receiver_with_imprecision(self, sim_max_game):
        game = sim_max_game
        game.confusion = game.similarity
        dynamics = QuantalResponseDynamics(5)
        sender_strategy = np.array([[0.3, 0.7], [0.4, 0.6]])
        receiver_strategy = np.array([[0.2, 0.8], [0.9, 0.1]])
        new_receiver_strategy = dynamics.update_receiver(sender_strategy, receiver_strategy, game)
        assert np.round(new_receiver_strategy, decimals=3).tolist() == [[0.852, 0.148], [0.938, 0.062]]
