const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

// 游戏变量
let plane = {
    x: 100,
    y: canvas.height / 2,
    width: 40,
    height: 40,
    targetY: canvas.height / 2
};

let keyState = {};

let obstacles = [];
let score = 0;
let gameOver = false;
let animationFrame;

// 常量
const MOVE_SPEED = 3;
const OBSTACLE_GAP = 200;
const OBSTACLE_WIDTH = 60;
const OBSTACLE_SPEED = 3;

// 初始化游戏
function initGame() {
    plane.y = canvas.height / 2;
    plane.speed = 0;
    obstacles = [];
    score = 0;
    gameOver = false;
    document.getElementById('gameOver').classList.add('hidden');
    updateGame();
}

// 绘制飞机
function drawPlane() {
    ctx.fillStyle = '#FF0000';
    ctx.fillRect(plane.x, plane.y, plane.width, plane.height);
}

// 生成障碍物
function createObstacle() {
    const gapStart = Math.random() * (canvas.height - OBSTACLE_GAP);
    obstacles.push({
        x: canvas.width,
        topHeight: gapStart,
        bottomHeight: canvas.height - gapStart - OBSTACLE_GAP,
        passed: false
    });
}

// 绘制障碍物
function drawObstacles() {
    ctx.fillStyle = '#008000';
    obstacles.forEach(obstacle => {
        // 上障碍物
        ctx.fillRect(obstacle.x, 0, OBSTACLE_WIDTH, obstacle.topHeight);
        // 下障碍物
        ctx.fillRect(obstacle.x, canvas.height - obstacle.bottomHeight, OBSTACLE_WIDTH, obstacle.bottomHeight);
    });
}

// 更新游戏状态
function updateGame() {
    if (gameOver) return;

    // 清空画布
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 更新飞机位置
    if (keyState['ArrowUp']) {
        plane.targetY -= MOVE_SPEED;
    }
    if (keyState['ArrowDown']) {
        plane.targetY += MOVE_SPEED;
    }
    
    // 限制飞机移动范围
    plane.targetY = Math.max(0, Math.min(canvas.height - plane.height, plane.targetY));
    
    // 平滑移动
    plane.y += (plane.targetY - plane.y) * 0.1;

    // 绘制元素
    drawPlane();
    drawObstacles();

    // 碰撞检测
    if (checkCollision()) {
        endGame();
        return;
    }

    // 更新障碍物
    updateObstacles();

    // 计分
    updateScore();

    animationFrame = requestAnimationFrame(updateGame);
}

// 碰撞检测
function checkCollision() {
    // 边界检测
    if (plane.y < 0 || plane.y + plane.height > canvas.height) {
        return true;
    }

    // 障碍物检测
    for (let obstacle of obstacles) {
        if (plane.x < obstacle.x + OBSTACLE_WIDTH &&
            plane.x + plane.width > obstacle.x &&
            (plane.y < obstacle.topHeight ||
            plane.y + plane.height > canvas.height - obstacle.bottomHeight)) {
            return true;
        }
    }
    return false;
}

// 更新障碍物
function updateObstacles() {
    // 移动障碍物
    obstacles.forEach(obstacle => {
        obstacle.x -= OBSTACLE_SPEED;
    });

    // 移除屏幕外的障碍物
    obstacles = obstacles.filter(obstacle => obstacle.x + OBSTACLE_WIDTH > 0);

    // 生成新障碍物
    if (obstacles.length === 0 || obstacles[obstacles.length - 1].x < canvas.width - 300) {
        createObstacle();
    }
}

// 更新分数
function updateScore() {
    obstacles.forEach(obstacle => {
        if (obstacle.x + OBSTACLE_WIDTH < plane.x && !obstacle.passed) {
            score++;
            obstacle.passed = true;
        }
    });
}

// 游戏结束
function endGame() {
    gameOver = true;
    cancelAnimationFrame(animationFrame);
    document.getElementById('finalScore').textContent = score;
    document.getElementById('gameOver').classList.remove('hidden');
}

// 重新开始游戏
function restartGame() {
    initGame();
}

// 事件监听
document.addEventListener('keydown', (e) => {
    if (e.code === 'ArrowUp' || e.code === 'ArrowDown') {
        keyState[e.code] = true;
    }
});

document.addEventListener('keyup', (e) => {
    if (e.code === 'ArrowUp' || e.code === 'ArrowDown') {
        keyState[e.code] = false;
    }
});

// 启动游戏
initGame();