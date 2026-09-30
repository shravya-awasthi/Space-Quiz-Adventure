# Helper functions

def get_ascii_ship():
    return r"""
                 /\
                /  \
               /____\
              |      |
              | NASA |
              |______|
               /||||\
              /_||||_\
             🚀  🚀  🚀

             *   .   *
        .  *   SPACE   .  *
    """


def clamp(value, minimum, maximum):
    # keeps value between minimum and maximum
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value
