
__all__ = ['get_dataset_config']

# Do not change this!
dataset_config = {

    'china' : {
        'seed'            : 512,
        'md5_indexs'      : 'f5a59dc9d39413df57d9119f5619a86d',
        'output'          : 'dataset_Shenzhen_splitted.csv',
        'nimages'         : 662,
        #'md5_images'      : 'e690adf29a28e42d5f500de792b73e30',
        'nimages_splitted': 59580,
    },

    'imageamento' : {
        'seed'            : 1,
        'md5_indexs'      : 'ef2e574529023af6e4b865c5e5d68234',
        'output'          : 'dataset_Imageamento_splitted.csv',
        'nimages'         : 170,
        'md5_images'      : 'a7fdfc87f01980583d5cb538def30e74',
        'nimages_splitted': 15300,
    },

}

def get_dataset_config(dataset_name):
    return dataset_config[dataset_name]
