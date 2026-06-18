import numpy as np

print("Task 1. fer => C")
def to_cel(temp):
    return (temp - 32)/1.8
to_cel_vect = np.vectorize(to_cel)
temperatures = [32, 68, 100, 212, 77]

print("Changed to celcius:", to_cel_vect(temperatures) )

print("\nTask 2. base ** power ")
def to_pow(base, power):
    return base ** power
to_pow_vect = np.vectorize(to_pow)
b = [2, 3, 4, 5]
p = [1, 2, 3, 4]

print("Increased to a power:", to_pow_vect(b, p))

print("\nTask 3. Solve the system of equations using `numpy`")

A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])

B = np.array([7, 4, 5])

result = np.linalg.solve(A, B)
print( """
the equation:
4x + 5y + 6z = 7 
3x - y + z = 4 
2x + y - 2z = 5
Solution:
""",result)

print("""
Task 4. Given the electrical circuit equations below, 
solve for $I_1, I_2, I_3$ (currents in the branches):

10I_1 - 2I_2 + 3I_3 = 12
-2I_1 + 8I_2 - I_3 = -5 
3I_1 - I_2 + 6I_3 = 15
""")
I = np.array([[10, -2, 3],
              [-2, 8, -1],
              [3, -1, 6]])

B = np.array([12, -5, 15])
result = np.linalg.solve(I, B)
print("solution : \n",result)


from PIL import Image

print("\nTask: Image Manipulation with NumPy and PIL")

img = Image.open("/home/zhav3n/Desktop/homework/Lesson 14/birds.jpg")
image_array = np.array(img)
print(image_array.shape)
print(image_array.dtype)

print("\n1. Flip the Image")

def flip_image(arr):
    flipped = arr[::-1, ::-1, :]
    return flipped

flipped_result = flip_image(image_array)
flipped_img = Image.fromarray(flipped_result)
flipped_img.save("/home/zhav3n/Desktop/homework/Lesson 14/flipped_birds.jpg")

print("\n2. Add Random Noise")

def add_noise(arr):
    noise = np.random.randint(-20, 20, size=arr.shape)
    noisy = arr.astype(int) + noise
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy

noisy_result = add_noise(image_array)
noisy_img = Image.fromarray(noisy_result)
noisy_img.save("/home/zhav3n/Desktop/homework/Lesson 14/noisy_birds.jpg")

print("\n3. Brighten Channels")

def brighten_channels(arr, channel=0, value=40):
    result = arr.copy()
    brightened = np.clip(arr[:, :, channel].astype(int) + value, 0, 255)
    result[:, :, channel] = brightened.astype(np.uint8)
    return result

brightened_result = brighten_channels(image_array, channel=0, value=40)
brightened_img = Image.fromarray(brightened_result)
brightened_img.save("/home/zhav3n/Desktop/homework/Lesson 14/brightened_birds.jpg")

# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).
# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.
# **Bonus Challenge**:
# - Create a function for each manipulation 
# (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) 
# to promote modularity and reusability of code.
# ---