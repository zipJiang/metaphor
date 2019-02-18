import os


def thu_sampler(thu_loc):
    # This function samples a subset from THUNews dataset
    thu_dir = os.listdir(thu_loc)
    for subdir in thu_dir:
        print (subdir)
