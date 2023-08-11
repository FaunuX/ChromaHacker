const myForm = document.getElementById('custom_form');
const addButton = document.getElementById('addButton');
const removeButton = document.getElementById('removeButton');

function convertButtonToArg(str) {
	  // Use a regular expression to match "button" followed by a number
	  const regex = /^button(\d+)$/;

	  // Check if the input string matches the expected pattern
	  if (regex.test(str)) {
		      // Extract the number from the string
		      const match = str.match(regex);
		      const number = match[1];

		      // Return the modified string "arg" + number
		      return number;
		    }

	  // Return the original string if it doesn't match the pattern
	  return str;
}


// Track the count of input elements
let inputCount = 0;

// Add event listener to the button
addButton.addEventListener('click', function(event) {
	// Create a new input element
	event.preventDefault(); // Prevent form submission
	const div = document.createElement('div');
	div.className = 'colorInputDiv';
	div.id = inputCount;
	const newInput = document.createElement('input');
	newInput.type = 'color';
	newInput.class = 'input';
	newInput.name = `arg${inputCount}`;
	newInput.id = `arg${inputCount}`;
	const newButton = document.createElement('button');
	newButton.type = 'button';
	// newInput.class = 'input';
	// newInput.name = `arg${inputCount}`;
	newButton.id = `button${inputCount}`;
	newButton.textContent = 'X'

	newButton.addEventListener('click', function(event) {
		// Create a new input element
		event.preventDefault(); // Prevent form submission
		const oldInput = document.getElementById(convertButtonToArg(newButton.id));
		console.log(document.getElementsByClassName('colorInputDiv'))
		const elements = [...document.getElementsByClassName('colorInputDiv')]
		elements.forEach(function(element) {
			if (element.id > oldInput.id) {
				id = element.id - 1;
				element.id = id;
				element.children[0].name = `arg${id}`;
				element.children[0].id = `arg${id}`;
				element.children[1].id = `button${id}`;
			}
		})

		oldInput.remove()
		inputCount--;

	});

	// Append the new input element to the form
	div.appendChild(newInput);
	div.appendChild(newButton);
	myForm.appendChild(div);


	// Increment the input count
	inputCount++;
});

function openForm(evt, name) {
	  // Declare all variables
	  var i, tabcontent, tablinks;

	  // Get all elements with class="tabcontent" and hide them
	  tabcontent = document.getElementsByTagName("form");
	  for (i = 0; i < tabcontent.length; i++) {
		      tabcontent[i].style.display = "none";
		    }

	  // Get all elements with class="tablinks" and remove the class "active"
	  tablinks = document.getElementsByClassName("tablinks");
	  for (i = 0; i < tablinks.length; i++) {
		      tablinks[i].className = tablinks[i].className.replace(" active", "");
		    }

	  // Show the current tab, and add an "active" class to the button that opened the tab
	  document.getElementById(name).style.display = "block";
	  evt.currentTarget.className += " active";
}
