// Define an array of objects to store checkbox data for gender
const genderCheckboxes = [
    {
      id: "male-checkbox",
      value: "male",
      icon: "fad fa-",
      title: "Male"
    },
    {
      id: "female-checkbox",
      value: "female",
      icon: "fa fa-",
      title: "Female"
    },
    // ...rest of the gender checkboxes
  ];
  
  // Define an array of objects to store checkbox data for activity level
  const activityCheckboxes = [
    {
      id: "sedentary-checkbox",
      value: "sedentary",
      icon: "fad fa-",
      title: "Sedentary"
    },
    {
      id: "lightly-active-checkbox",
      value: "lightly active",
      icon: "fa fa-",
      title: "Lightly Active"
    },
    {
      id: "moderately-active-checkbox",
      value: "moderately active",
      icon: "fa fa-",
      title: "Moderately Active"
    },
    {
      id: "very-active-checkbox",
      value: "very active",
      icon: "fa fa-",
      title: "Very Active"
    },
    // ...rest of the activity level checkboxes
  ];
  
  // Function to dynamically add checkboxes to the page
  function addCheckboxes(checkboxes, containerId) {
    const checkboxList = document.getElementById(containerId);
    checkboxes.forEach(checkbox => {
      const checkboxElement = document.createElement("div");
      checkboxElement.className = "form-element";
      checkboxElement.id = checkbox.id;
  
      const inputElement = document.createElement("input");
      inputElement.type = "checkbox";
      inputElement.name = containerId; // Use containerId as the name to differentiate the sets
      inputElement.value = checkbox.value;
      inputElement.id = checkbox.value;
      inputElement.addEventListener("change", handleCheckboxChange);
  
      const labelElement = document.createElement("label");
      labelElement.htmlFor = checkbox.value;
  
      const iconElement = document.createElement("div");
      iconElement.className = "icon";
      const icon = document.createElement("i");
      icon.className = checkbox.icon;
      iconElement.appendChild(icon);
  
      const titleElement = document.createElement("div");
      titleElement.className = "title";
      titleElement.textContent = checkbox.title;
  
      labelElement.appendChild(iconElement);
      labelElement.appendChild(titleElement);
      checkboxElement.appendChild(inputElement);
      checkboxElement.appendChild(labelElement);
      checkboxList.appendChild(checkboxElement);
    });
  }
  
  // Call the addCheckboxes function to initially display the checkboxes for gender and activity level
  addCheckboxes(genderCheckboxes, "checkbox-list-1");
  addCheckboxes(activityCheckboxes, "checkbox-list-2");
  console.log("Hello")
  // Function to handle checkbox change event
  function handleCheckboxChange(event) {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      if (checkbox !== event.target && checkbox.name === event.target.name) {
        checkbox.checked = false;
      }
    });
  }

  
  function sendSelectedCheckboxes() {
    console.log("Hello");
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/process_data", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
      }
    };
  
    const genderData = document.querySelectorAll("#checkbox-list-1 input[type='checkbox']:checked");
    const selectedGenderCheckbox = Array.from(genderData).map(checkbox => checkbox.value);
  
    const activityData = document.querySelectorAll("#checkbox-list-2 input[type='checkbox']:checked");
    const selectedActivityCheckbox = Array.from(activityData).map(checkbox => checkbox.value);
  
    console.log("Selected Gender Checkbox:", selectedGenderCheckbox);
    console.log("Selected Activity Checkbox:", selectedActivityCheckbox);
  
    const send_data = JSON.stringify({
      data: {
        gender: selectedGenderCheckbox[0],
        activity: selectedActivityCheckbox[0],
      },
    });
    xhr.send(send_data);
  }
  
  