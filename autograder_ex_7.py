def compute_average_spam_confidence(filename):
    count = 0
    total_confidence = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('X-DSPAM-Confidence:'):
                    count += 1
                    confidence = float(line.split(':')[1].strip())
                    total_confidence += confidence

        if count > 0:
            average_confidence = total_confidence / count
            return average_confidence
        else:
            return 0.0

    except FileNotFoundError:
        print("File not found.")
        return None

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    average_spam_confidence = compute_average_spam_confidence(file_name)
    if average_spam_confidence is not None:
        print(f"Average spam confidence: {average_spam_confidence:.4f}")
