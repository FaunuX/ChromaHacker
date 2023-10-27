import { useState, useEffect, useRef } from 'react'

import '@blueprintjs/core/lib/css/blueprint.css';
import { FormGroup, ControlGroup, InputGroup, Button, Divider } from '@blueprintjs/core'

import ColorsList from './ColorsList.tsx'

const UseColorscheme = () => {
	return (
			<InputGroup 
				name="colorscheme" 
				type="search" 
				placeholder="Search?" 
				leftIcon="search"
				className="ml-8"
			/>
	       )
}

const CustomColors = ({onChange}) => {
	const [colors, setColors] = useState([])

	useEffect(() => {
		onChange({target: {value: colors}})
	}, [colors])

	const addColorSelect = (event) => {
		setColors(currentColors => {
			return [
				...currentColors,
				{value: "#000000", id: crypto.randomUUID()}
			]
		})
	}

	const ColorInput = ({value, id}) => {
		return (
			<>
			<Divider className="invisible"/>
			<InputGroup 
				onChange={updateColorValue} type="color" value={value} id={id} 
				className="block"
			/>
			</>
		)
	}
	
	const updateColorValue = (event) => {
		const target = event.target
		const value = target.value
		const id = target.id
		setColors(currentColors => {
			return currentColors.map(col => {
				if (col.id == id)  {
					return {value: value, id: id}
				} else {
					return col
				}
			})
		})
	}

	return (
			<ControlGroup className="flex flex-col bp5-dark">
			<Button icon="plus" onClick={ addColorSelect } /> {colors.map(col => { 
				const id = col.id.toString()
				return (
						<ColorInput value={col.value} id={id} key={id} />
				)
			})}
			</ControlGroup>
		)
}

const FromImage = () => {
	return (
			<InputGroup 
				name="color_image_url" 
				type="url" 
				placeholder="Enter URL for your Image"
				className="ml-8"
			/>
		)
}

export { UseColorscheme, CustomColors, FromImage }

