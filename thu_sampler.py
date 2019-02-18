import os
import random


def thu_sampler(thu_loc, sample_loc="../data/THUsamples", k=100):
    """This function samples a subset from THUNews dataset"""
    thu_dir = os.listdir(thu_loc)
    for subdir in thu_dir:
        print ("sampling data from ... {}".format(subdir))
        sub_loc = os.path.join(thu_loc, subdir)
        subdir_files = os.listdir(sub_loc)

        subsample_loc = os.path.join(sample_loc, subdir)
        print ("writing to: P{}".format(subsample_loc))
        os.makedirs(subsample_loc)

        file_samples = random.sample(subdir_files, k)
        for target_f in file_samples:
            target_loc = os.path.join(sub_loc, target_f)
            target_file = open(target_loc, 'r')
            s_loc = os.path.join(subsample_loc, target_f)
            sample_file = open(s_loc, 'w')
            for line in target_file:
                sample_file.write(line)

            target_file.close()
            sample_file.close()


if __name__ == '__main__':
    thu_sampler('../data/THUCNews/')
