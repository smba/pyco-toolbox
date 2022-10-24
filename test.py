import unittest

import pycosa.modeling as modeling
import pycosa.sampling as sampling
import pycosa.util as util
import pycosa.lib as lib

import itertools

import numpy as np
import pandas as pd

import os

import matplotlib.pyplot as plt

"""
Testing should include aspects like
- Sample size
    - negative
    - exact
    - maximum not exceeded
- Uniqueness



class TestSingleSampler(unittest.TestCase):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")


class TestBDDSamplerSampler(TestSingleSampler):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")

    def test_sample(self):
        sampler = sampling.BDDSampler(self.fm)
        sampler.constrain_enabled(["COMPRESS"])
        sampler.constrain_disabled(["DEFRAG_ALWAYS"])
        sample = sampler.sample(size=300)
        # print(sample)
        self.assertTrue(sample["DEFRAG_ALWAYS"].values.sum() == 0)
        self.assertTrue(sample["COMPRESS"].values.sum() == sample.shape[0])


class TestDistanceBasedSampler(TestSingleSampler):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")

    def test_sample(self):
        sampler = sampling.DistanceBasedSampler(self.fm)
        sample = sampler.sample(size=50)


class TestCoverageSampler(TestSingleSampler):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")

    def test_sample(self):
        sampler = sampling.CoverageSampler(self.fm)
        sample = sampler.sample(t=1)
        sample = sampler.sample(t=2)
        sample = sampler.sample(t=1, negwise=True)
        sample = sampler.sample(t=2, negwise=True)


class TestDFSSampler(TestSingleSampler):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")

    def test_sample(self):
        sampler = sampling.DFSSampler(self.fm)
        sample = sampler.sample(size=100)


class TestDiversitySampler(TestSingleSampler):
    def setUp(self):
        self.fm = modeling.CNFExpression()
        self.fm.from_dimacs("_test_data/feature_models/h2.dimacs")

    def test_sample(self):
        sampler = sampling.DiversityPromotionSampler(self.fm)
        sample = sampler.sample(size=100)


class TestOfflineSampler(unittest.TestCase):
    def setUp(self):

        N = 10
        options = np.arange(N)
        self.options = options

        np.random.seed(1)
        df = np.random.choice([0, 1], size=(10000, N))
        df = np.unique(df, axis=0)

        df = pd.DataFrame(df, columns=options)
        self.df = df

    def test_ee_sampling_optionwise(self):
        sampler = sampling.OfflineSampler(self.df)

        # feature wise
        for o in self.options:
            options = [o]
            en, dis = sampler.elementary_effect_sample(options, size=5)

            # show that the indices are different
            self.assertTrue(len(en) == len(dis))
            self.assertTrue(en != dis, "Indexes are identical!")
            for i in range(len(en)):
                self.assertTrue(en[i] != dis[i], "{} != {}".format(en[i], dis[i]))

            # show that option $o is different
            for i in range(len(en)):
                cfg1 = self.df.loc[en[i]]
                cfg2 = self.df.loc[dis[i]]
                self.assertTrue(cfg1[o] != cfg2[o])

                # check that configurations only differ in exactly one column
                distance = np.count_nonzero(cfg1 != cfg2)
                self.assertTrue(distance == 1)

    def test_ee_sampling_pairwise(self):
        sampler = sampling.OfflineSampler(self.df)

        # feature wise
        for opt in itertools.combinations(self.options, 2):
            options = list(opt)
            en, dis = sampler.elementary_effect_sample(options, size=5)

            # show that the indices are different
            self.assertTrue(len(en) == len(dis))
            self.assertTrue(en != dis, "Indexes are identical!")
            for i in range(len(en)):
                self.assertTrue(en[i] != dis[i], "{} != {}".format(en[i], dis[i]))

            # show that option $o is different
            for i in range(len(en)):
                cfg1 = self.df.loc[en[i]]
                cfg2 = self.df.loc[dis[i]]
                for o in options:
                    self.assertTrue(cfg1[o] != cfg2[o])

                # check that configurations only differ in exactly one column
                distance = np.count_nonzero(cfg1 != cfg2)
                self.assertTrue(distance == 2)


class TestElementaryEffectSampler(unittest.TestCase):
    def setUp(self):

        # load feature models from test data
        tdata = "./_test_data/feature_models/"
        self.fms = []
        for file in os.listdir(tdata):
            path = tdata + file
            fm = modeling.CNFExpression()
            fm.from_dimacs(path)
            self.fms.append(fm)

    def test_foo(self):
        for seed in range(2):
            for noptions in range(1, 2):
                np.random.seed(seed)
                for fm in self.fms:
                    optionals = fm.find_optional_options()["optional"]

                    options = np.random.choice(optionals, size=noptions)
                    options = [fm.index_map[i] for i in options]

                    sampler = sampling.ElementaryEffectSampler(fm)

                    try:
                        en, dis = sampler.sample(10, options)
                    except lib.SatisfiabilityExhaustionError:
                        print(
                            "exhausted at seed {} and #options of {}".format(
                                seed, noptions
                            )
                        )


class UtilTester(unittest.TestCase):
    def test_construct_categorical_variable(self):
        df = pd.DataFrame(
            np.random.choice(np.arange(10), size=(100, 10)),
            columns=[str(i) for i in range(10)],
        )

        for c in df.columns:
            df = util.construct_categorical_variable(df, c)
"""

if __name__ == "__main__":
    unittest.main()
