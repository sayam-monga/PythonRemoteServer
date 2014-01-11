class Arguments(object):

    def argument_should_be_correct(self, argument, expected):
        expected = eval(expected)
        if argument != expected:
            raise AssertionError('%r != %r' % (argument, expected))

    def no_arguments(self):
        return self._format()

    def one_argument(self, arg):
        return self._format(arg)

    def two_arguments(self, arg1, arg2):
        return self._format(arg1, arg2)

    def six_arguments(self, arg1, arg2, arg3, arg4, arg5, arg6):
        return self._format(arg1, arg2, arg3, arg4, arg5, arg6)

    def arguments_with_default_values(self, arg1, arg2='2', arg3=3):
        return self._format(arg1, arg2, arg3)

    def variable_number_of_arguments(self, *args):
        return self._format(*args)

    def required_defaults_and_varargs(self, req, default='world', *varargs):
        return self._format(req, default, *varargs)

    def _format(self, *args):
        return ', '.join(str(a) for a in args)


if __name__ == '__main__':
    import sys
    from robotremoteserver import RobotRemoteServer

    RobotRemoteServer(Arguments(), '127.0.0.1', *sys.argv[1:])
