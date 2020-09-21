// Set constraints for the video stream
var constraints = { video: { facingMode: "environment" }, audio: false };
var track = null;

// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
    cameraTrigger = document.querySelector("#camera--trigger"),
    form = document.querySelector("#form"),
    input= document.querySelector('#input');

// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
            track = stream.getTracks()[0];
            cameraView.srcObject = stream;
            cameraView.width = window.innerWidth;
            cameraView.height = window.innerHeight;
        })
        .catch(function(error) {
            console.error("Oops. Something is broken.", error);
        });

}

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);

    cameraOutput.src = cameraSensor.toDataURL("image/webp");

    input.value = `${cameraSensor.toDataURL("image/webp")}`;
    form.submit();
    cameraOutput.classList.add("taken");
    // track.stop();
};

window.addEventListener("load", cameraStart, false);