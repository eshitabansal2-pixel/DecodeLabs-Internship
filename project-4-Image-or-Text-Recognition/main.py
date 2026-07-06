import cv2
import pytesseract
import re
import json

pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = cv2.imread("images/receipt.jpg")
if img is None:
    print(" ERROR: Image not found. Check file path and name.")
    exit()

# Resize the image
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# Show original image
cv2.imshow("Original Image", img)
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Show grayscale image
cv2.imshow("Grayscale Image", gray)
# Remove noise using Gaussian Blur
blur = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imshow("Blurred Image", blur)
# Thresholding (BLACK & WHITE conversion)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# custom config goes here
custom_config = r'--oem 3 --psm 6'
# ocr (after config)
text = pytesseract.image_to_string(thresh, config=custom_config)
lines = text.split("\n")
receipt_data = {
    "items": [],
    "grand_total": None
}

for line in lines:
    match = re.search(r'([A-Za-z ]+)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)', line)

    if match:
        receipt_data["items"].append({
            "name": match.group(1).strip(),
            "qty": float(match.group(2)),
            "price": float(match.group(3)),
            "total": float(match.group(4))
            })
    if "total" in line.lower():
        numbers = re.findall(r'\d+\.\d+|\d+', line)
        if numbers:
            receipt_data["grand_total"] = float(numbers[-1])

            print("\n===== RECEIPT SUMMARY =====")

for item in receipt_data["items"]:
    print(f"Item: {item['name']}")
    print(f"Quantity: {item['qty']}")
    print(f"Price: ₹{item['price']}")
    print(f"Total: ₹{item['total']}")
    print("-------------------------")

print("Grand Total:", receipt_data["grand_total"])

with open("receipt_data.json","w") as file:
    json.dump(receipt_data, file, indent=4)
    print("Receipt data saved to receipt_data.json")
# Show threshold image
cv2.imshow("Threshold Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

