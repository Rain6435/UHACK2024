interface PreviewProps {
  image: string;
  width?: number;
  height?: number;
}

const Preview: React.FC<PreviewProps> = (props) => {
  return (
    <div>
      <div className="w-max rounded m-4">
        <h1>Preview:</h1>
        <div className="flex w-full mt-2">
          <img
            className={
              props.width && props.height
                ? `rounded w-[${props.width}px] h-[${props.height}px]`
                : props.width
                ? `rounded w-[${props.width}px]`
                : props.height
                ? `rounded h-[${props.height}px]`
                : "rounded w-[200px]"
            }
            src={props.image}
          />
        </div>
      </div>
    </div>
  );
};

export default Preview;
