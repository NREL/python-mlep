import pytest

import mlep


class TestMlepProcess:
    def test_initialize(self):
        ep = mlep.MlepProcess()
        assert ep is not None
        assert ep.is_running is False


class TestSocketRead:
    def test_is_not_running(self):
        # -- Setup
        ep = mlep.MlepProcess()
        data = ep.read()

        # -- Assert empty byte string
        assert data == b''

    def test_set_running(self):
        # -- Setup
        ep = mlep.MlepProcess()
        ep.is_running = True
        data = ep.read()

        # -- Assert empty byte string
        # There is still no comm_socket, so
        # an empty byte string is returned
        assert data == b''

    # Regardless of the receive size, the data received
    # should always be the same
    @pytest.mark.parametrize('receive_size',
                             [1, 2, 6, 50, 1000, 4096])
    def test_read(self, create_server_socket, create_client_socket, receive_size):
        # -- Setup
        ep = mlep.MlepProcess()

        # Create mockup of the server socket
        ep.server_socket = create_server_socket
        ep.is_running = True

        # The client socket represents the bcvtb side of things
        bcvtb_socket = create_client_socket

        data_to_send = b'sdfa\n'
        bcvtb_socket.sendall(data_to_send)

        # accept the connection
        ep.comm_socket, ep.client_address = ep.server_socket.accept()
        data = ep.read(receive_size)

        assert data == data_to_send
        ep.server_socket.close()
