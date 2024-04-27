import React from "react";
import { useNavigate } from "react-router-dom";

export interface BaseProps {
  title: string;
  message: string;
  componentName: string;
  redirect?:string|undefined;
}

const BaseDialog: React.FC<BaseProps> = (props) => {
  const navigate = useNavigate();
  function Exit(){
    if(props.redirect){
      navigate(props.redirect);
    }
  }
  return (
    <div>
      <dialog id={props.componentName} className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg mb-3">{props.title}</h3>
          <p className="">{props.message}</p>
          <div className="modal-action">
            <form method="dialog" onSubmit={Exit}>
              <button className="btn">Close</button>
            </form>
          </div>
        </div>
      </dialog>
    </div>
  );
};

export default BaseDialog;
