import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

model = tf.keras.models.load_model("model1_v3")
classes = [
    'apoderus_javanicus', 
    'aulacaspis_tubercularis', 
    'ceroplastes_rubens',
    'cisaberoptus_kenyae', 
    'dappula_tertia', 
    'dialeuropora_decempuncta', 
    'erosomyia_sp', 
    'icerya_seychellarum', 
    'ischnaspis_longirostris', 
    'mictis_longicornis', 
    'neomelicharia_sparsa', 
    'normal', 
    'orthaga_euadrusalis', 
    'procontarinia_matteiana', 
    'procontarinia_rubus', 
    'valanga_nigricornis'
]

def predict_class(filename):
    # img = cv.resize(cv.imread(filename), [128, 128])
    # actual_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    image = tf.io.read_file(filename)
    image = tf.io.decode_image(image)
    image = tf.image.resize(image, [128, 128])
    transformed = tf.reshape(image, [1, 128, 128, 3])
    # print(dir(model))
    prediction = model.predict(transformed)
    print(prediction[0].argmax())
    return classes[prediction.argmax(axis=-1)[0]]

# print(predict_class("x.jpg"))