
function blinkInput() {
  const blinkInputs = [
    ...document.querySelectorAll("[data-module='blink-input']")
  ];

  blinkInputs.forEach(function(input) {
    const elInput = input.querySelector("[data-module='blink-input-el']");
    const inputCursor = input.querySelector(
      "[data-module='blink-input-cursor']"
    );
    const inputText = input.querySelector("[data-module='blink-input-text']");
    const inputTextShort = input.querySelector(
      "[data-module='blink-input-text-short']"
    );
    const inputWarning = input.querySelector(
      "[data-module='blink-input-warning']"
    );
    let inputActive;

    const findPosition = function(isDelete) {
      let textArray = [];

      for (let i = 0; i < elInput.selectionStart; i++) {
        textArray.push(elInput.value[i]);
      }

      elInput.selectionStart = textArray.length;
      inputTextShort.innerText = textArray.join("");

      inputCursor.setAttribute(
        "style",
        `left: ${inputTextShort.clientWidth}px`
      );
    };

    elInput.addEventListener("focusout", () =>
      inputCursor.setAttribute("style", `left: 0`)
    );

    elInput.addEventListener("click", findPosition);

    input.addEventListener("keyup", function(event) {
      const charCode = event.which || event.keyCode;
      const charStr = String.fromCharCode(charCode);

      if (charCode === 8) {
        findPosition("isDelete");
        inputText.innerText = elInput.value;
      }

      if (!/[a-z0-9]/i.test(charStr) || charCode !== 32) {
        inputActive = true;
        findPosition();
      }
    });

    elInput.addEventListener("keyup", function(event) {
      if (inputActive) {
        inputText.innerText = elInput.value;
        inputTextShort.innerText = elInput.value;
        inputCursor.setAttribute("style", `left: ${inputText.clientWidth}px`);
      }
    });
  });
}

blinkInput();
$(document).ready(function() {


    var content = $('.content');
    var currentItem = content.filter('.active');
    var steps = $('.card').filter('.steps');
    var inactive1 = $('.inactive-1');
    var inactive2 = $('.inactive-2');

    $('.button').click(function() {
        var nextItem = currentItem.next();
        var lastItem = content.last();
        var contentFirst = content.first();

        currentItem.removeClass('active');

        if (currentItem.is(lastItem)) {
            currentItem = contentFirst.addClass('active');
            currentItem.css({'right': '10%', 'opacity': '1'});
            $('.step').animate({width: '33%'});
            inactive1.animate({height: '8px', marginLeft:'20px', marginRight:'20px'}, 100);
            inactive2.animate({height: '8px', marginLeft:'10px', marginRight:'10px'}, 100);

        } else if (currentItem.is(contentFirst)) {
            currentItem.animate({opacity: 0}, 1000);
            currentItem = nextItem.addClass('active');
            $('.step').animate({width: '66%'});
            inactive2.animate({height: '0', marginLeft:'0px', marginRight:'0px'}, 100);

        } else {
            currentItem = nextItem.addClass('active');
            $('.step').animate({width: '100%'});
            inactive1.animate({height: '0', marginLeft:'0px', marginRight:'0px'}, 100);
        }
    });

});
