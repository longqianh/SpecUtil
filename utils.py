from skimage.color import rgb2xyz, xyz2rgb


def interp(data):
    # 31->301
    data = torch.Tensor(data)
    data = nn.functional.interpolate(
        data, size=301, mode='linear', align_corners=True)
    return data


def hsi2rgb(hsi):
    cmf = np.loadtxt('xyz.txt', usecols=(1, 2, 3))
    cmf = cmf[40:40 + 301, :]
    xyz = hsi @ cmf

    xyz /= xyz.max()
    rgb = xyz2rgb(xyz)

    return rgb


def show_rgb(data):
    data_rgb = hsi2rgb(data)
    plt.imshow(data_rgb)
    plt.show()


def plot_error_image(data, pred):

    error = abs(np.mean((pred - data) / data, axis=-1))
    shw = plt.imshow(error)
    bar = plt.colorbar(shw)
    bar.set_label('Error')
    plt.show()
