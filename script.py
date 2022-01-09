import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

model = tf.keras.models.load_model("model1_v3")
classes = [
    'Apoderus Javanicus', 
    'Aulacaspis Tubercularis', 
    'Ceroplastes Rubens',
    'Cisaberoptus Kenyae', 
    'Dappula Tertia', 
    'Dialeuropora Decempuncta', 
    'Erosomyia Sp', 
    'Icerya Seychellarum', 
    'Ischnaspis Longirostris', 
    'Mictis Longicornis', 
    'Neomelicharia Sparsa', 
    'Normal', 
    'Orthaga Euadrusalis', 
    'Procontarinia Matteiana', 
    'Procontarinia Rubus', 
    'Valanga Nigricornis'
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