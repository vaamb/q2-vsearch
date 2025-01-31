import os

import skbio

from qiime2.plugin.testing import TestPluginBase
from qiime2.util import redirected_stdio
from q2_types.feature_data import DNAFASTAFormat

from q2_vsearch._subsample import subsample


class SubsampleTests(TestPluginBase):
    package = 'q2_vsearch.tests'

    def setUp(self):
        super().setUp()
        input_sequences_fp = self.get_data_path('dna-sequences-1.fasta')
        self.input_sequences = DNAFASTAFormat(input_sequences_fp, mode='r')
        self.input_sequences_list = [*skbio.io.read(
            str(self.input_sequences), constructor=skbio.DNA, format='fasta')]

    def test_subsample(self):
        with redirected_stdio(stderr=os.devnull):
            obs_sequences = subsample(
                sequences=self.input_sequences, sample_size=2, random_seed=42)

        obs_seqs = skbio.io.read(
            str(obs_sequences), constructor=skbio.DNA, format='fasta')
        exp_seqs = [
            self.input_sequences_list[0],
            self.input_sequences_list[3],
        ]
        self.assertEqual([*obs_seqs], exp_seqs)
