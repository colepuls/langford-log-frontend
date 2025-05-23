# Langford Log - Foreman Log App

The **Langford Log** is a cross-platform mobile app that allows construction foremen to log daily job activity, assign hours to workers, attach photos (like receipts and delivery tickets), and submit a completed log directly to the company via email.

Built with **React Native** and **Node.js**, and deployed via **Render** for 24/7 accessibility.

---

## 🚀 Features

- ✅ Cross-platform: Android + iOS support
- ✅ Auto-formatted date input (MM/DD/YYYY)
- ✅ Employee directory with dropdown selection (max 10)
- ✅ Input work hours per employee
- ✅ Add a description of the day's work
- ✅ Upload up to 10 compressed photos
- ✅ Sends log directly via email (using Nodemailer)
- ✅ Form resets after successful submission
- ✅ Fully hosted backend (Render)

---

## 📲 Mobile Tech Stack

- [Expo](https://expo.dev) (React Native CLI)
- `expo-image-picker` (select and compress images)
- `react-native-masked-text` (smart date formatting)
- `@react-native-picker/picker` (dropdown for employee selection)

---

## 🔧 Backend Stack

- Node.js + Express
- Multer (file upload handling)
- Nodemailer (email sending)
- Hosted on [Render](https://render.com)

---

## 📸 Screenshots

*Coming soon – add screenshots in `frontend/screenshots/` and update paths here.*

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/colepuls/langford-log.git
cd langford-log
```

### 2. Start the frontend (Expo)

```bash
cd frontend
npm install
npx expo start
```

Scan the QR code with **Expo Go** or build it using `eas build`.

### 3. Start the backend (Node.js)

```bash
cd backend
npm install
node index.js
```

Or deploy to [Render](https://render.com) for 24/7 access.

---

## 📤 Deployment

- Backend is deployed via [Render](https://langford-log-backend.onrender.com)
- Frontend can be deployed using **EAS Build** or installed via **TestFlight** and direct `.apk`

---

## 📧 How It Works

1. Foreman fills out the log
2. Selects employees from dropdown (with hour inputs)
3. Adds optional photos
4. Submits log
5. App sends form + files to backend
6. Backend emails completed log to company

---

## 🔒 Security & Notes

- All sensitive credentials (email/password) stored as environment variables
- FormData automatically handles image compression
- Render free tier is used, but you can upgrade to prevent cold starts

---

## ✨ Planned Features

- [ ] Email + password login (for identifying sender)
- [ ] PDF summary of the log
- [ ] Save past logs history
- [ ] Admin portal to view all submissions

---

## 👨‍💻 Author

Made by [Cole Puls](https://github.com/colepuls)  
Contact: [colepuls@me.com](mailto:colepuls@me.com)

---

## 📄 License

MIT License
