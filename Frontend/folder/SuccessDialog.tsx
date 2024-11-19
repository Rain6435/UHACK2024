import React from "react";
import { useNavigate } from "react-router-dom";
import ClipboardIcon from "../../assets/ClipboardIcon";

export interface Props {
  title: string;
  message: string;
  componentName: string;
  redirect?: string | undefined;
  reportId: string;
}

const SuccessDialog: React.FC<Props> = (props) => {
  const navigate = useNavigate();
  function Exit() {
    if (props.redirect) {
      navigate(props.redirect);
    }
  }
  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(props.reportId);
    } catch (error: any) {
      throw error;
    }
  };
  return (
    <div>
      <dialog id={props.componentName} className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg mb-3">{props.title}</h3>
          <p className="">{props.message}</p>
          <div className="flex my-4">
            <div className="my-auto">
              <p>{props.reportId}</p>
              <button className="btn btn-outline" onClick={copyToClipboard}>
                <ClipboardIcon></ClipboardIcon>
              </button>
            </div>
            <div className="modal-action my-auto ml-auto">
              <form method="dialog" onSubmit={Exit}>
                <button className="btn">Close</button>
              </form>
            </div>
          </div>
        </div>
      </dialog>
    </div>
  );
};

export default SuccessDialog;
