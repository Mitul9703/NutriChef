import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
import { getFirestore, collection, addDoc, doc,setDoc} from "https://www.gstatic.com/firebasejs/9.4.0/firebase-firestore.js";

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

// Function to save user information to Firestore
async function saveUserInfo(name, email, password, age, gender, activity, height, weight, targetWeight,vegetarian) {
  console.log("saveUserInfo function called");
  try {
    const usersCollection = collection(db, "users");
    const userDoc = doc(usersCollection, email);
    await setDoc(userDoc, {
      name: name,
      username: email,
      password: password,
      age: age,
      gender: gender,
      activity: activity,
      height: height,
      weight: weight,
      'Targetweight': targetWeight,
      vegetarian:vegetarian
    });

    const username = email;
    const details ={
      name: name,
      password: password,
      age: age,
      gender: gender,
      activity: activity,
      height: height,
      weight: weight,
      'Targetweight': targetWeight,
      vegetarian :vegetarian

    }
    const response = await fetch('/user_data.json', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({username,details})
    });
    console.log("User information saved successfully");
    window.location.assign("main_page")
  } catch (error) {
    console.log("Error saving user information:", error);
  }
}

// Function to handle form submission
function submitForm(event) {
  event.preventDefault();

  // Get the input values
  const name = document.getElementById("name").value;
  const email = document.getElementById("mail").value;
  const password = document.getElementById("passwd").value;
  const age = parseInt(document.getElementById("age").value);
  const gender = document.getElementById("gender").value;
  const activity = document.getElementById("activity").value;
  const height = parseInt(document.getElementById("height").value);
  const weight = parseInt(document.getElementById("weight").value);
  const targetWeight = parseInt(document.getElementById("target-weight").value);

  const vegetarianValue = document.getElementById("vegetarian").value;
  const vegetarian = vegetarianValue === "true";

  // Save the user information to Firestore
  saveUserInfo(name, email, password, age, gender, activity, height, weight, targetWeight,vegetarian);
  
  
  
}

// Add an event listener to the form submission
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOMContentLoaded event fired");

  const signupForm = document.querySelector("form");
  signupForm.addEventListener("submit", submitForm);
});