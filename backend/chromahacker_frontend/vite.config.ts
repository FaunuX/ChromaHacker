import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],
	server: {
		proxy: {
			'/palettize_from_image': {
				target: 'http://localhost:5000',
				changeOrigin: true,
				secure: false,      
				ws: true,
			},
			'/palettize_premade': {
				target: 'http://localhost:5000',
				changeOrigin: true,
				secure: false,      
				ws: true,
			},
			'/palettize_custom': {
				target: 'http://localhost:5000',
				changeOrigin: true,
				secure: false,      
				ws: true,
			}
		}
	}
})
