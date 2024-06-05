import * as THREE from 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.module.js';
import { Tiff } from 'https://unpkg.com/tiff.js/dist/tiff.min.js';

const tiffDirectory = 'ImageFiles'; // Directory containing TIFF images

async function loadTIFFImages(directory) {
    const fileNames = await fetch(`${directory}/index.json`).then(response => response.json());
    const images = [];

    for (const fileName of fileNames) {
        const response = await fetch(`${directory}/${fileName}`);
        const arrayBuffer = await response.arrayBuffer();
        const tiff = new Tiff({ buffer: arrayBuffer });
        const canvas = tiff.toCanvas();
        images.push(canvas);
    }

    return images;
}

function create3DScene(images) {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry();
    const materials = images.map(image => new THREE.MeshBasicMaterial({
        map: new THREE.CanvasTexture(image),
        side: THREE.DoubleSide
    }));

    const cube = new THREE.Mesh(geometry, materials);
    scene.add(cube);

    camera.position.z = 5;

    function animate() {
        requestAnimationFrame(animate);
        cube.rotation.x += 0.01;
        cube.rotation.y += 0.01;
        renderer.render(scene, camera);
    }

    animate();
}

async function main() {
    const images = await loadTIFFImages(tiffDirectory);
    create3DScene(images);
}

main();
