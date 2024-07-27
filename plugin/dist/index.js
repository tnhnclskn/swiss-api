const mainContainer = document.getElementById("main-container");
const formContainer = document.getElementById("form-container");
const topImage = document.getElementById("top-image");
const topTitle = document.getElementById("top-title");
const heading = document.getElementById("heading");
const paragraph = document.getElementById("paragraph");
const formAction = document.getElementById("form-action");
const resultContainer = document.getElementById("result-container");
const resultHeading = document.getElementById("result-heading");
const resultSign = document.getElementById("result-sign");
const errorContainer = document.getElementById("error-container");
const errorMessage = document.getElementById("error-message");
const calBtn = document.getElementById("cal-btn");

let formType = "";

const API_URL = "YOUR_API_URL"; 

[formContainer, resultContainer, errorContainer].forEach(el => el.style.display = "none");

const showForm = (title, imageSrc, type) => {
  formContainer.style.display = "block";
  mainContainer.style.display = "none";

  topImage.src = imageSrc;
  topTitle.innerText = title;
  heading.innerText = `What Is My ${type} Sign?`;
  paragraph.innerText = `
    If you are unsure of your ${type} sign, then use our ${type} sign calculator to look up in which constellation ${type} was located at the moment of your birth:
  `;

  formType = type;
};

const handleSubmit = async (e) => {
  e.preventDefault();
  errorContainer.style.display = "none";
  errorMessage.innerText = "";
  calBtn.disabled = true;
  calBtn.innerText = "Calculating...";

  try {
    const fname = document.getElementById("fname").value;
    const city = document.getElementById("city").value;
    const dob = document.getElementById("dob").value;
    const timeOfBirth = document.getElementById("timeOfBirth").value;
    const unknownTime = document.getElementById("unknownTime").checked;

    if (!fname || !city || !dob || (!unknownTime && !timeOfBirth)) {
      throw new Error("Please fill all fields");
    }

    const [year, month, day] = dob.split("-");
    const data = {
      name: fname,
      place_of_birth: city,
      dob: `${day}/${month}/${year}`,
      time: unknownTime ? "00:00" : timeOfBirth,
    };

    const response = await fetch(`${API_URL}/calculate_chart`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    const sign = result.planets[formType]?.sign;

    if (sign) {
      resultSign.innerText = `Your ${formType} sign is ${sign}`;
      resultContainer.style.display = "block";
      formAction.style.display = "none";
      mainContainer.style.display = "none";
      resultHeading.innerText = "Your Result:";
    } else {
      throw new Error(`Unable to determine ${formType} sign`);
    }

  } catch (error) {
    errorContainer.style.display = "block";
    errorMessage.innerText = error.message;
  } finally {
    calBtn.disabled = false;
    calBtn.innerText = "Calculate";
  }
};

const backHandler = () => {
  const isFormVisible = formContainer.style.display === "block";
  const isResultVisible = resultContainer.style.display === "block";

  if (isFormVisible) {
    if (isResultVisible) {
      resultContainer.style.display = "none";
    } else {
      formContainer.style.display = "none";
      mainContainer.style.display = "block";
    }
    errorContainer.style.display = "none";
    formAction.style.display = "block";
  }
};

formAction.addEventListener("submit", handleSubmit);