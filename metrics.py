import numpy as np


def MSE(x, x_hat):
    mse = np.sum((x - x_hat)**2) / len(x)
    return mse


def MRAE(x, x_hat):
    # Mean relative absolute error
    mrae = np.sum(np.abs((x - x_hat) / x)) / len(x)
    return mrae


def GFC(x, x_hat):
    # Goodness of fit coefficient
    x_normed = x / np.sqrt(np.sum(x**2))
    x_hat_normed = x_hat / np.sqrt(np.sum(x_hat**2))
    gfc = np.dot(x_normed, x_hat_normed)
    return gfc


def PSNR(v_max, x, x_hat):
    return 20 * np.log10(v_max / MRAE(x, x_hat))


if __name__ == '__main__':
    x = np.array([-1, 2, 3, 4, 5, 6, 7, 8])
    x_hat = np.array([-1.1, 2, 3.1, 4, 4.5, 7, 7.1, 8])
    print(MRAE(x, x_hat), MRAE(x * 10, x_hat * 10))
    print(GFC(x, x_hat), GFC(x * 10, x_hat * 10))
