// JQuery 2.1.4
// @codekit-prepend "../js-plugins/jquery-2.1.4.js"

// http://stackoverflow.com/questions/920236/how-can-i-detect-if-a-selector-returns-null
$.fn.exists = function () {
    return this.length !== 0;
}

// Bootstrap 3.3.4 JS
// @codekit-append "../js-plugins/affix.js"
// @codekit-append "../js-plugins/affix.js"
// @codekit-append "../js-plugins/alert.js"
// @codekit-append "../js-plugins/button.js"
// @codekit-append "../js-plugins/carousel.js"
// @codekit-append "../js-plugins/collapse.js"
// @codekit-append "../js-plugins/dropdown.js"
// @codekit-append "../js-plugins/modal.js"
// @codekit-append "../js-plugins/tooltip.js"
// @codekit-append "../js-plugins/popover.js"
// @codekit-append "../js-plugins/scrollspy.js"
// @codekit-append "../js-plugins/tab.js"
// @codekit-append "../js-plugins/transition.js"

// Bootstrap-datetimepicker
// @codekit-append "../js-plugins/moment-with-locales.js"
// @codekit-append "../js-plugins/bootstrap-datetimepicker.js"

// Django-ajax
// @codekit-append "../js-plugins/jquery.ajax.js"

// Autocomplete-light extra widgets
HospitalWidget = {
    getValue: function (choice) {
        // TODO: Secure this input so that it doesn't execute the contents of value!
        var value = choice.data('value');

        if (value == 'create') {
            choice.html(this.input.val())

            $.ajax(this.autocomplete.url, {
                async: false,
                type: 'post',
                data: {
                    'name': this.input.val(),
                },
                success: function (text, jqXHR, textStatus) {
                    value = text;
                }
            });

            choice.data('value', value);
        }

        return value;
    }
}