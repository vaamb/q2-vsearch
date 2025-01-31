from q2_types.feature_data import DNAFASTAFormat

from ._cluster_features import run_command


def subsample(
        sequences: DNAFASTAFormat,
        sample_size: int = 1000,
        random_seed: int = 0,
) -> DNAFASTAFormat:
    output = DNAFASTAFormat()
    cmd = [
        'vsearch',
        '--fastx_subsample', str(sequences),
        '--sample_size', str(sample_size),
        '--randseed', str(random_seed),
        '--fastaout', str(output),
    ]
    run_command(cmd)
    return output
