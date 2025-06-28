let Agnirva_tasks = JSON.parse(localStorage.getItem('Agnirva_tasks')) || [];
let Agnirva_editIndex = null;

const Agnirva_taskForm = document.getElementById('Agnirva_taskForm');
const Agnirva_taskTitle = document.getElementById('Agnirva_taskTitle');
const Agnirva_taskCategory = document.getElementById('Agnirva_taskCategory');
const Agnirva_taskPriority = document.getElementById('Agnirva_taskPriority');
const Agnirva_taskDeadline = document.getElementById('Agnirva_taskDeadline');
const Agnirva_taskBody = document.getElementById('Agnirva_taskBody');

function Agnirva_renderTasks() {
  Agnirva_taskBody.innerHTML = '';
  Agnirva_tasks.forEach((Agnirva_task, Agnirva_index) => {
    const Agnirva_row = document.createElement('tr');

    const Agnirva_titleCell = document.createElement('td');
    Agnirva_titleCell.textContent = Agnirva_task.title;
    Agnirva_row.appendChild(Agnirva_titleCell);

    const Agnirva_categoryCell = document.createElement('td');
    Agnirva_categoryCell.textContent = Agnirva_task.category;
    Agnirva_row.appendChild(Agnirva_categoryCell);

    const Agnirva_priorityCell = document.createElement('td');
    Agnirva_priorityCell.textContent = Agnirva_task.priority;
    Agnirva_row.appendChild(Agnirva_priorityCell);

    const Agnirva_deadlineCell = document.createElement('td');
    Agnirva_deadlineCell.textContent = Agnirva_task.deadline;
    Agnirva_row.appendChild(Agnirva_deadlineCell);

    const Agnirva_actionsCell = document.createElement('td');
    const Agnirva_editBtn = document.createElement('button');
    Agnirva_editBtn.className = 'edit-btn';
    Agnirva_editBtn.textContent = 'Edit';
    Agnirva_editBtn.onclick = () => Agnirva_editTask(Agnirva_index);

    const Agnirva_deleteBtn = document.createElement('button');
    Agnirva_deleteBtn.className = 'delete-btn';
    Agnirva_deleteBtn.textContent = 'Delete';
    Agnirva_deleteBtn.onclick = () => Agnirva_deleteTask(Agnirva_index);

    Agnirva_actionsCell.appendChild(Agnirva_editBtn);
    Agnirva_actionsCell.appendChild(Agnirva_deleteBtn);
    Agnirva_row.appendChild(Agnirva_actionsCell);

    Agnirva_taskBody.appendChild(Agnirva_row);
  });
}

Agnirva_taskForm.addEventListener('submit', (Agnirva_e) => {
  Agnirva_e.preventDefault();
  const Agnirva_title = Agnirva_taskTitle.value.trim();
  const Agnirva_category = Agnirva_taskCategory.value.trim();
  const Agnirva_priority = Agnirva_taskPriority.value;
  const Agnirva_deadline = Agnirva_taskDeadline.value;

  if (!Agnirva_title || !Agnirva_category || !Agnirva_priority || !Agnirva_deadline) return;

  const Agnirva_newTask = {
    title: Agnirva_title,
    category: Agnirva_category,
    priority: Agnirva_priority,
    deadline: Agnirva_deadline
  };

  if (Agnirva_editIndex === null) {
    Agnirva_tasks.push(Agnirva_newTask);
  } else {
    Agnirva_tasks[Agnirva_editIndex] = Agnirva_newTask;
    Agnirva_editIndex = null;
  }

  Agnirva_saveTasks();
  Agnirva_renderTasks();
  Agnirva_taskForm.reset();
});

function Agnirva_editTask(Agnirva_index) {
  Agnirva_editIndex = Agnirva_index;
  const Agnirva_task = Agnirva_tasks[Agnirva_index];
  Agnirva_taskTitle.value = Agnirva_task.title;
  Agnirva_taskCategory.value = Agnirva_task.category;
  Agnirva_taskPriority.value = Agnirva_task.priority;
  Agnirva_taskDeadline.value = Agnirva_task.deadline;
}

function Agnirva_deleteTask(Agnirva_index) {
  Agnirva_tasks.splice(Agnirva_index, 1);
  Agnirva_saveTasks();
  Agnirva_renderTasks();
}

function Agnirva_saveTasks() {
  localStorage.setItem('Agnirva_tasks', JSON.stringify(Agnirva_tasks));
}

Agnirva_renderTasks();
