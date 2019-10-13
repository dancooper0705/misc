import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras as keras

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_images = None
train_labels = None
test_image = None
test_labels = None
model = None
train_images_data = None
test_images_data = None

def plot_train_images():
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.tight_layout()
    plt.show()

def download_images():
    global test_images
    global test_labels
    global train_images
    global train_labels
    global test_images_data
    global train_images_data
    (train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    train_images_data = train_images.reshape(train_images.shape[0], 32*32*3)
    test_images_data = test_images.reshape(test_images.shape[0], 32*32*3)
    train_labels = train_labels.reshape(len(train_labels))
    test_labels = test_labels.reshape(len(test_labels))
    '''
    print('type(tain_lables): ' + str(type(train_labels)))
    print('train_images.shape: ' + str(train_images.shape))
    print('train_labels.shape: ' + str(train_labels.shape))
    print('test_images.shape: ' + str(test_images.shape))
    print('train_images_data.shape: ' + str(train_images_data.shape))
    print('test_images_data.shape: ' + str(test_images_data.shape))
    print('train_images: ' + str(train_images))
    print('train_labels: ' + str(train_labels))
    print('test_images: ' + str(test_images))
    '''

def learn_train_images():
    global model
    inputs = keras.Input(shape=(32*32*3,), name='img')
    x = keras.layers.Dense(64, activation='relu')(inputs)
    x = keras.layers.Dense(64, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)
    model = keras.Model(inputs=inputs, outputs=outputs, name='mnist_model')
    model.summary()
    model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
    model.fit(train_images_data, train_labels, epochs=5, validation_split=0.2, steps_per_epoch=train_images_data.shape[0]//10)
    test_scores = model.evaluate(test_images_data,  test_labels, verbose=2)
    print('Test loss:', test_scores[0])
    print('Test accuracy:', test_scores[1])

def predict_all_test_images():
    predictions = model.predict(test_images_data)
    print(predictions[0])
    print(np.argmax(predictions[0]))
    print(test_labels[0])
    # Plot the first X test images, their predicted labels, and the true labels.
    # Color correct predictions in blue and incorrect predictions in red.
    num_rows = 5
    num_cols = 3
    num_images = num_rows*num_cols
    plt.figure(figsize=(2*2*num_cols, 2*num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2*num_cols, 2*i+1)
        plot_image(i, predictions[i], test_labels, test_images)
        plt.subplot(num_rows, 2*num_cols, 2*i+2)
        plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()
    plt.show()

def predict_single_test_images():
    img = test_images_data[0]
    print(img.shape)
    # Add the image to a batch where it's the only member.
    img = (np.expand_dims(img,0))
    print(img.shape)
    predictions = model.predict(img)
    print(predictions)
    i = 0
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions[0], test_labels, test_images)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions[0], test_labels)
    plt.show()

def save_model_as_image():
    keras.utils.plot_model(model, 'model_with_shape_info.png', show_shapes=True)

def main():
    download_images()
    learn_train_images()
    save_model_as_image()
    plot_train_images()
    predict_all_test_images()
    predict_single_test_images()

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

if __name__ == "__main__":
    main()
