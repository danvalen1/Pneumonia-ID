import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap

fontscale = 1.5
sns.set(font_scale=fontscale, style='whitegrid')
figsize = (12,8)

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
    
def subsetsJoint(index_df):
    jointplot = sns.jointplot(data=index_df, 
                           x="width", 
                           y="height", 
                           hue="data_set_name", 
                           kind="scatter",
                           height = figsize[1],
                           ratio = round(figsize[1]/figsize[0]+5),
                           alpha=0.4)


    jointplot.ax_joint.legend(title="Subset")
    jointplot.ax_joint.set_xlabel("Width of Image")
    jointplot.ax_joint.set_ylabel("Height of Image")
    jointplot.ax_joint.set_ylabel("Height of Image")
    plt.suptitle("Distribution of Image Dimensions\nby Data Subset Membership", size=18)
    
    plt.tight_layout()
    plt.savefig("images/image_pix_dist.png")
    
    return plt.show()
