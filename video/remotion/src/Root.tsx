import React from 'react';
import {Composition} from 'remotion';
import {Titre} from './Titre';

export const RemotionRoot: React.FC = () => {
	return (
		<Composition
			id="Titre"
			component={Titre}
			durationInFrames={90}
			fps={30}
			width={1920}
			height={1080}
		/>
	);
};
