function info_consent(consentCheckBox) {
    if(consentCheckBox.checked) {
        document.getElementById("next_button").disabled = false;
    }
    else {
        document.getElementById("next_button").disabled = true;
    }
}

function serviceModalDisplay() {
    document.getElementById("service-modal").style.display = "flex";
    document.getElementById("service-modal").style.tabindex = "0";
}

function serviceModalClose() {
    document.getElementById("service-modal").style.display = "none";
    document.getElementById("service-modal").style.tabindex = "-1";

}