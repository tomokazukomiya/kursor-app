# Kursor

Kursor Customizer is a cross-platform open-source desktop application that allows users to customize their cursor's appearance, including size, color, and icon. Built with Electron for the frontend and Python for backend functionality, this app provides a seamless experience for personalizing your cursor on Windows, macOS, and Linux.

## Features
- **Custom Cursor Size**: Adjust the cursor size using a slider.
- **Custom Cursor Icons**: Upload and apply custom cursor icons.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **User-Friendly Interface**: A sleek, modern UI inspired by Apple's design language.
- **Persistent Settings**: Save your preferences for future use.

## Installation

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- pip (Python package manager)

### Steps
#### Clone the Repository:
```bash
git clone https://github.com/your-username/cursor-customizer.git
cd cursor-customizer
```

#### Install Node.js Dependencies:
```bash
npm install
```

#### Install Python Dependencies:
```bash
pip install -r requirements.txt
```

#### Run the Application:
```bash
npm start
```

## Usage

### Adjust Cursor Size:
- Use the slider to change the cursor size.
- Click **Apply Changes** to save your settings.

### Upload Custom Cursor Icons:
- Click **Upload Cursor** to select a custom cursor icon (.cur or .ani files).
- Apply the icon to change your cursor appearance.

### Reset to Default:
- Use the **Reset** button to restore the default cursor settings.

## Development

### Running in Development Mode
#### Start the Electron app:
```bash
npm start
```

#### For hot-reloading during development, use:
```bash
npm run dev
```

### Packaging the App
#### Install electron-packager:
```bash
npm install electron-packager --save-dev
```

#### Package the App:
##### For Windows:
```bash
npx electron-packager . --platform=win32 --arch=x64
```

##### For macOS:
```bash
npx electron-packager . --platform=darwin --arch=x64
```

##### For Linux:
```bash
npx electron-packager . --platform=linux --arch=x64
```

#### Distribute the App:
The packaged app will be located in the `out` directory.

## Contributing
Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **Electron** for the cross-platform desktop framework.
- **Bootstrap** for the sleek UI components.
- **Python** for backend functionality.

## Support
If you encounter any issues or have questions, please open an issue.

Enjoy -tommy
