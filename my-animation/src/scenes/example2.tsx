import {makeScene2D, Circle} from '@motion-canvas/2d';
import {all, createRef} from '@motion-canvas/core';

export default makeScene2D(function* (view) {
  const myCircle = createRef<Circle>();

  view.add(
    <Circle
      ref={myCircle}
      // try changing these properties:
      x={100}
      y={100}
      width={140}
      height={140}
      fill="#e13238"
    />,
  );

 // yield* all(
  //  myCircle().position.y(-200, 5).to(100, 0.98),
  //  myCircle().fill('#e6a700', 1).to('#e13238', 1),
  // );
  yield * myCircle().position.y(-200,3).to(100,0.8)
});
