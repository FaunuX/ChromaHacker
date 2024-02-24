import { useState, useEffect } from 'react'

import '@blueprintjs/core/lib/css/blueprint.css';
import { ControlGroup, InputGroup, Button, Divider } from '@blueprintjs/core'

type Color = {
	value: string;
	id: any;
}

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

const CustomColors = ({onChange}: any) => {
	const [colors, setColors] = useState<Color[]>([])

	useEffect(() => {
		onChange({target: {value: colors}})
	}, [colors])

	const addColorSelect = (_event: any) => {
		setColors(function (currentColors: any) {
			return [
				...currentColors,
				{value: "#000000", id: crypto.randomUUID()}
			]
		})
	}

	const ColorInput = ({value, id}: any) => {
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
	
	const updateColorValue = (event: any) => {
		const target = event.target
		const value = target.value
		const id = target.id
		setColors(currentColors => {
			return currentColors.map(col => {
				console.log(col);
				if (col["id"] == id)  {
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

export { UseColorscheme, CustomColors }

