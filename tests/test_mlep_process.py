import mlep


class TestMlepProcess:
    def test_initialize(self):
        ep = mlep.MlepProcess()
        assert ep is not None
