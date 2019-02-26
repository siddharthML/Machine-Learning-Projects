import math
import numpy as np
from scipy.stats import multivariate_normal


def construct_data(nsamples, dataset, problem, plusminus=False):
    """Construct a dataset.

    Parameters
    ----------
    nsamples : int
      Number of samples in the dataset.
    dataset : 'train' or 'test'
      Whether the dataset is used for training or testing. Simply changes the
      seed of the random generator.
    problem : 'linear' or 'nonlinear'
      Selects the probability distributions accordingly.
    plusminus : bool, optional
      Whether the labels should be in {0,1} or {-1,1}.
    """
    assert dataset in ('train', 'test')
    if dataset == 'train':
        # Training points are randomly generated(sampled); this ensures
        # we'll get the same samples.
        np.random.seed(0)
    elif dataset == 'test':
        np.random.seed(500)

    assert problem in ('linear', 'nonlinear')
    if problem == 'linear':
        distribution_1 = construct_distribution('gaussian_21_1')
        distribution_2 = construct_distribution('mixture_1')
    elif problem == 'nonlinear':
        distribution_1 = construct_distribution('mixture_2')
        distribution_2 = construct_distribution('mixture_3')

    samples_1 = sample_distribution(distribution_1, nsamples // 2)
    samples_2 = sample_distribution(distribution_2, nsamples // 2)

    x_rng = np.linspace(0, 1, 50)
    y_rng = np.linspace(0, 1, 50)
    unscaled_posterior_1 = eval_unscaled_posterior_on_grid(
            x_rng, y_rng, distribution_1)
    unscaled_posterior_2 = eval_unscaled_posterior_on_grid(
            x_rng, y_rng, distribution_2)
    posterior = 1 / (1 + unscaled_posterior_2 / unscaled_posterior_1)

    # Gather all
    features = np.concatenate([samples_1, samples_2])
    labels = np.zeros(nsamples)
    labels[:samples_1.shape[0]] = 1

    idxs = np.random.permutation(features.shape[0])
    features = features[idxs]
    labels = labels[idxs]

    if plusminus:
        labels = 2 * labels - 1
    else:
        features = np.hstack([features, np.ones(features.shape[0])])

    return features, labels, posterior


def rot2D(angle):
    """Return a 2D rotation matrix of the given angle."""
    c = math.cos(angle)
    s = math.sin(angle)
    return np.array([[c, -s], [s, c]])


def construct_distribution(distr_name):
    """Define the parameters of the distribution (mean, covariance, prior).

    Returns
    -------
    out : list of dicts
      Sequence of {'mean', 'cov', 'prior'} dicts. The list contains more
      than one dict in the case of a mixture of distributions.

    """
    if distr_name == 'gaussian_11_1':
        mean = np.array([5, 4.2]).reshape(1, 2)
        # covariance = u*s*u'
        # s: lengths of principal axes
        # u: rotation matrix
        s = np.diag([2, .1])
        th = math.pi / 4
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'gaussian_11_2':
        mean = np.array([4.2, 5]).reshape(1, 2)
        # covariance
        s = np.diag([3, .1])
        th = math.pi / 8
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'gaussian_12_1':
        mean = np.array([0, 0]).reshape(1, 2)
        s = np.diag([2, .1])
        th = 0
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'gaussian_12_2':
        mean = np.array([0, 0]).reshape(1, 2)
        s = np.diag([2, .1])
        th = math.pi / 2
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'gaussian_21_1':
        mean = np.array([.6, .6]).reshape(1, 2)
        s = .2 * np.diag([.1, .01])
        th = -math.pi / 8
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'gaussian_21_2':
        mean = np.array([.5, .5]).reshape(1, 2)
        s = .2 * np.diag([.1, .01])
        th = -math.pi / 8
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.ones(1)
    elif distr_name == 'mixture_1':
        mean = np.array([[.5, .5],
                         [.5, .1]])
        s = .2 * np.diag([.1, .01])
        th = -math.pi / 8
        u = rot2D(th)
        cov = u @ s @ u.T
        prior = np.array([.8, .2])
    elif distr_name == 'mixture_2':
        mean = np.array([[.4, .8],
                         [.4, .3],
                         [.6, .4]])
        cov = np.eye(mean.shape[1]) * .01
        prior = np.ones(3) / 3
    elif distr_name == 'mixture_3':
        mean = np.array([[.8, .2],
                         [.8, .5],
                         [.2, .2],
                         [.4, .6]])
        cov = np.eye(mean.shape[1]) * .01
        prior = np.ones(4) / 4
    else:
        print("Invalid distribution name")

    return [{'mean': mi, 'cov': cov, 'prior': pi}
            for mi, pi in zip(mean, prior)]


def sample_distribution(distr, nsamples):
    """Randomly sample points from the input distribution.

    Parameters
    ----------
    distr : list of dicts
      Distribution as returned by construct_distribution.
    nsamples : int
      Number of points to sample.

    Returns
    -------
    out : (nsamples, ndims) numpy array
      Where ndims is the number of dimensions of the sampling space.

    """
    # Randomly sample values in [0, 1)
    rand_01 = np.random.rand(nsamples)
    # Make bins from accumulated prior values
    bins = [0] + np.cumsum([d['prior'] for d in distr]).tolist()
    # Count number of elements in each bin
    count = np.histogram(rand_01, bins)[0]
    # Draw each number of values from each multivariate Gaussian distribution
    samples_agg = []
    for d, c in zip(distr, count):
        samples = np.random.multivariate_normal(d['mean'], d['cov'], c)
        samples_agg.append(samples)
    # Concatenate and return samples
    return np.concatenate(samples_agg)


def eval_unscaled_posterior_on_grid(x_rng, y_rng, distr):
    """Evaluate the unscaled posterior of the distribution on a rectangular
    2D grid.

    Parameters
    ----------
    x_rng : (n,) sequence
      Range of values along the first axis.
    y_rng : (n,) sequence
      Range of values along the second axis.
    distr : list of dicts
      Distribution as returned by construct_distribution.

    Returns
    -------
    val : (n, n) numpy array
      Values of the unscaled posterior on the grid.

    """
    grid_x, grid_y = np.meshgrid(x_rng, y_rng)
    xy_arr = np.column_stack([grid_x.flat, grid_y.flat])

    val = sum(multivariate_normal.pdf(xy_arr, d['mean'], d['cov']) * d['prior']
              for d in distr)
    val = val.reshape(grid_x.shape)
    return val


if __name__ == "__main__":
    f, l, p = construct_data(10, 'train', 'nonlinear', plusminus=True)
    print(f)
    print(l)
    print(p)
