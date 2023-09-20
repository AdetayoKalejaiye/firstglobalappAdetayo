const canvas = document.getElementById('drawing-board');
const toolbar = document.getElementById('toolbar');
const noteInput = document.getElementById('note-input');
const addNoteButton = document.getElementById('add-note');
const notesContainer = document.getElementById('notes-container');
const drawingBoard = document.getElementById('canvas-div');
const hydrogenHub1 = document.getElementById('hydrogen-hub-1');
const hydrogenHub2 = document.getElementById('hydrogen-hub-2');
const dialogContainer = document.getElementById('dialog-container');


const ctx = canvas.getContext('2d');
const canvasOffsetX = canvas.offsetLeft;
const canvasOffsetY = canvas.offsetTop;

canvas.width = window.innerWidth - canvasOffsetX;
canvas.height = window.innerHeight - canvasOffsetY;

let isPainting = false;
let isErasing = false;
let lineWidth = 5;
let startX;
let startY;

// Define the positions for hiding and showing the hydrogen hubs
const hiddenPosition = '-100px'; // Adjust as needed
const visiblePositiontop1 = '70%'; // Adjust as needed
const visiblePositiontop2 = '70%'; // Adjust as needed
const visiblePositionleft1 = '45%'; // Adjust as needed
const visiblePositionleft2 = '65%'; // Adjust as needed

// Define the background images for the two toggle states
// Define the background images for the two toggle states
const hiddenBackground = 'url("/static/img/PlayingField.png")';
const visibleBackground = 'url("/static/img/PlayingFieldHidden.png")';



let isHubsDraggable = false;

hydrogenHub1.style.left = visiblePositionleft1;
hydrogenHub1.style.top = visiblePositiontop1;
hydrogenHub2.style.left = visiblePositionleft2;
hydrogenHub2.style.top = visiblePositiontop2;
hydrogenHub1.style.visibility = 'hidden';
hydrogenHub2.style.visibility = 'hidden';
drawingBoard.style.backgroundImage = hiddenBackground;        

function showBubble() {
    const hubRect = hydrogenHub1.getBoundingClientRect();
    
    // Update the position of the dialog box to follow the hub
    dialogContainer.style.left = hubRect.right - canvasOffsetX + 'px'; // Adjust the position as needed
    dialogContainer.style.top = hubRect.bottom + 'px'; // Adjust the position as needed
    dialogContainer.style.display = 'block';
    setTimeout(() => {
        dialogContainer.style.display = 'none';
    }, 3000); // Close the bubble after 5 seconds
}

//dragging function
function dragElement(elmnt) {
    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
    
    elmnt.onmousedown = dragMouseDown;
    
    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        
        document.onmouseup = closeDragElement;
        
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }
    
    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }
    
    function closeDragElement() {
        /* stop moving when mouse button is released:*/
        document.onmouseup = null;
        document.onmousemove = null;
    }
}


document.getElementById('draggableHubs').addEventListener('change', () => {
    isHubsDraggable = document.getElementById('draggableHubs').checked;
    
    // Call the appropriate function based on the isHubsDraggable state
    if (isHubsDraggable) {
        hydrogenHub1.style.visibility = 'visible';
        hydrogenHub2.style.visibility = 'visible';
        
        // // Reset their positions to the default
        
        // If draggable is active, enable drag for the hydrogen hubs
        dragElement(document.getElementById('hydrogen-hub-1'));
        dragElement(document.getElementById('hydrogen-hub-2'));
        
        // Change the background image of .drawing-board
        drawingBoard.style.backgroundImage = visibleBackground;
        showBubble()
    } else {
        
        
        // Change the background image of .drawing-board
        
        // If draggable is not active, remove event listeners from the hydrogen hubs
        document.getElementById('hydrogen-hub-1').onmousedown = null;
        document.getElementById('hydrogen-hub-2').onmousedown = null;
        
        
    }
});


// Combine the add note and create note functionality
const addNoteAndCreate = () => {
    const noteText = noteInput.value.trim();
    
    if (noteText) {
        const noteElement = document.createElement('div');
        noteElement.classList.add('note');
        
        const editText = document.createElement('input');
        editText.type = 'text';
        editText.value = noteText;
        editText.readOnly = true; // Make it non-editable by default
        
        const editButton = document.createElement('button');
        editButton.innerHTML = "&#9998;"; // Unicode pencil icon
        editButton.title = 'Edit';
        editButton.classList.add('edit-button');
        let isEditing = false; // Track whether editing is active or not
        
        editButton.addEventListener('click', () => {
            if (isEditing) {
                // If already editing, save changes and exit edit mode
                const updatedText = editText.value;
                noteText.textContent = updatedText;
                isEditing = false;
                editText.readOnly = true; // Make it non-editable again
                editButton.style.backgroundColor = ''; // Remove green background
                editButton.style.color = ''; // Remove white text color
            } else {
                // If not editing, enter edit mode
                isEditing = true;
                editText.readOnly = false;
                editButton.style.backgroundColor = 'green'; // Green background
                editButton.style.color = 'white'; // White text color
            }
        });
        
        const deleteButton = document.createElement('button');
        deleteButton.innerHTML = "&#128465;"; // Unicode dustbin icon
        deleteButton.title = 'Delete';
        deleteButton.classList.add('delete-button');
        deleteButton.addEventListener('click', () => {
            noteElement.remove();
        });
        
        noteElement.appendChild(editText); // Add an input field for editing
        noteElement.appendChild(editButton);
        noteElement.appendChild(deleteButton);
        
        notesContainer.appendChild(noteElement);
        noteInput.value = ''; // Clear the input field
    }
};


document.getElementById('add-note').addEventListener('click', addNoteAndCreate);



toolbar.addEventListener('click', (e) => {
    if (e.target.id === 'clear') {
        hydrogenHub1.style.visibility = 'hidden';
        hydrogenHub2.style.visibility = 'hidden';
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawingBoard.style.backgroundImage = hiddenBackground
        
        
        // Move them to the hidden positions
        hydrogenHub1.style.left = visiblePositionleft1;
        hydrogenHub1.style.top = visiblePositiontop1;
        hydrogenHub2.style.left = visiblePositionleft2;
        hydrogenHub2.style.top = visiblePositiontop2;
        document.getElementById('draggableHubs').checked = false;
        isHubsDraggable = false;
    }
    
    if (e.target.id === 'eraser') {
        isErasing = !isErasing;
        if (isErasing) {
            e.target.classList.add('active');
        } else {
            e.target.classList.remove('active');
        }
        
        ctx.globalCompositeOperation = isErasing ? 'destination-out' : 'source-over';
    }
});

toolbar.addEventListener('change', (e) => {
    if (e.target.id === 'stroke') {
        ctx.strokeStyle = e.target.value;
        if (isErasing) {
            isErasing = false;
            document.getElementById('eraser').classList.remove('active');
        }
    }
    
    if (e.target.id === 'lineWidth') {
        lineWidth = e.target.value;
    }
});

const draw = (e) => {
    if (!isPainting || (isErasing && !isPainting) || noteInput === document.activeElement) {
        return;
    }
    
    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';
    const currentX = e.clientX - canvasOffsetX;
    const currentY = e.clientY - canvasOffsetY;
    
    ctx.lineTo(currentX, currentY);
    ctx.stroke();
};

canvas.addEventListener('mousedown', (e) => {
    isPainting = true;
    startX = e.clientX - canvasOffsetX;
    startY = e.clientY - canvasOffsetY;
    ctx.beginPath();
    
    if (isErasing) {
        ctx.globalCompositeOperation = 'destination-out';
    } else {
        ctx.globalCompositeOperation = 'source-over';
    }
});

canvas.addEventListener('mouseup', () => {
    isPainting = false;
    ctx.closePath();
});

canvas.addEventListener('mousemove', draw);

