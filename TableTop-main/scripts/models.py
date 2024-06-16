import pyray as ray
import os

class Models:

    def __init__(self) -> None:
        pass
        
        
    def load_models(array, num, path):
        path_completed = f'{path}{num}.vox'

        model = ray.load_model(path_completed)

        #Compute model translation matrix to center model on draw position (0, 0 , 0)
        bb = ray.get_model_bounding_box(model)
        center = (ray.Vector3) (0, 0, 0)
        center.x = bb.min.x + (((bb.max.x - bb.min.x) / 2))
        center.z = bb.min.z + (((bb.max.z - bb.min.z) / 2))

        matTranslate = ray.matrix_translate(-center.x, 0, -center.z)
        model.transform = matTranslate
        
        array.append(model)
        
        return array

    def verifying_models(num, path):
        exists = 0
        
        path_completed = f'{path}{num}.vox'

        if os.path.exists(path_completed):
            exists = 1

        return exists
