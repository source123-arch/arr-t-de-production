import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';

export const Titre: React.FC = () => {
	const frame = useCurrentFrame();
	const opacity = interpolate(frame, [0, 30], [0, 1], {extrapolateRight: 'clamp'});

	return (
		<AbsoluteFill
			style={{
				backgroundColor: '#111',
				color: 'white',
				justifyContent: 'center',
				alignItems: 'center',
				fontSize: 100,
				fontFamily: 'sans-serif',
				opacity,
			}}
		>
			Espace confiné
		</AbsoluteFill>
	);
};
