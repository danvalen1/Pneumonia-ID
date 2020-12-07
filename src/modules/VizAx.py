import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

fontscale = 2
sns.set(font_scale=fontscale, style='whitegrid')

def channelScatter(index_df):
    grey_img = index_df[index_df.channels == 1]
    color_img = index_df[index_df.channels == 3]

    fig, ax = plt.subplots(figsize = (12,8))

    ax.scatter(x=grey_img.width, y=grey_img.height, label="greyscale", color="grey", alpha = 0.1)
    ax.scatter(x=color_img.width, y=color_img.height, label="color", color="purple", alpha = 0.1)
    ax.set(xlabel = "Width of Image",
           ylabel = "Height of Image",
           Title = "Dimensions of Images Colored by Image Type"
          )

    plt.legend()
    
    plt.savefig("images/image_colors.png")
    return plt.show()
    