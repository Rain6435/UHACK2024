/**
 * Converts a File object to a base64-encoded string.
 * @param file The File object to be converted.
 * @returns A Promise that resolves with the base64-encoded string representation of the file.
 */
export async function fileToBase64(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    // Create a new FileReader instance
    const reader = new FileReader();

    // Set up event handlers for successful file reading and error handling
    reader.onload = () => {
      // When the file reading is successful, resolve the promise with the base64 string
      const base64String:string = reader.result as string;
      resolve(base64String);
    };

    reader.onerror = reject; // If there's an error during reading, reject the promise

    // Read the file as a data URL (base64-encoded)
    reader.readAsDataURL(file);
  });
}
