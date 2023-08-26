import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
import { getFirestore, getDocs, collection, doc, getDoc } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js";

const firebaseConfig = {
    apiKey: "AIzaSyAXsMwkBDgb_QiNg2K0YEQO17sIrTEdDkI",
    authDomain: "adsproj-f1323.firebaseapp.com",
    projectId: "adsproj-f1323",
    storageBucket: "adsproj-f1323.appspot.com",
    messagingSenderId: "965335056438",
    appId: "1:965335056438:web:a49dc10b5634968c6a9897",
    measurementId: "G-2E4H8SHFKK"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Get user data from Firestore
async function getUserData(username) {
  const usersCollection = collection(db, "users");
  const userDoc = doc(usersCollection, username);
  const userData = await getDoc(userDoc);
  if (userData.exists()) {
    return userData.data();
  } else {
    return null;
  }
}

async function getUserDetails(username) {
    const usersCollection = collection(db, "users");
    const userDoc = doc(usersCollection, username);
    const userData = await getDoc(userDoc);
    if (userData.exists()) {
      return userData.data();
    } else {
      return null;
    }
  }

// Verify login credentials
async function verifyLogin(username, password) {
  const userData = await getUserData(username);
  if (userData && userData.password === password) {
    const details = await getUserDetails(username);
    try {
        const response = await fetch('/user_data.json', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({username,details})
        });
    
        if (response.ok) {
          const result = await response.json();
          console.log('Meal added successfully:', meal);
        } else {
          console.log('Failed to add meal:', response.status);
        }}
        catch (error) {
            console.log('Error adding meal:', error);
          }
    return true;
  } else {
    return false;
  }
}

const hideOnLoaderElements = document.querySelectorAll(".page-container");
hideOnLoaderElements.forEach(element => {
  element.style.display = "none";
});

// Handle the form submission
function login(event) {
  event.preventDefault();


  const hideOnLoaderElements1 = document.querySelectorAll(".page-container");
  hideOnLoaderElements1.forEach(element => {
    element.style.display = "flex";
  });
  // Show the loader while verifying
  const loader = document.getElementById("loader");
  loader.style.display = "block";



  const hideOnLoaderElements = document.querySelectorAll(".hide-on-loader");
  hideOnLoaderElements.forEach(element => {
    element.style.display = "none";
  });

  // Get the input values
  const username = document.getElementById("username-input").value;
  const password = document.getElementById("password-input").value;
  const error_container = document.getElementById("error-container")

  // Verify the login credentials
  verifyLogin(username, password)
    .then((isLoggedIn) => {

      loader.style.display = "none";


      if (isLoggedIn) {
        // Login successful, redirect to the homepage
        hideOnLoaderElements.forEach(element => {
          element.style.display = "block";
        });
        window.location.href = "main_page";
      } else {
        // Login failed, display an error message
        console.log("Invalid username or password");
        error_container.textContent ="Invalid username or password" 
      }
    })
    .catch((error) => {
      console.log("Error verifying login credentials:", error);
    });
}

// Add an event listener to the form submission
const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", login);
