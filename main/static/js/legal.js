function info_consent(consentCheckBox) {
    if(consentCheckBox.checked) {
        document.getElementById("next_button").disabled = false;
    }
    else {
        document.getElementById("next_button").disabled = true;
    }
}