import React from 'react'

function Imagehelper({product}) {
    const imageurl = product ? product.image : `https://cdn.dribbble.com/users/596121/screenshots/2011231/mongoose_800x600_144dpi.png?compress=1&resize=800x600`

    return (
        <div className="rounded border border-success p-2">
            <img src={imageurl}
            style={{maxWidth:"100%",maxHeight:"100%"}}
            className="mb-3 rounded" 
            alt=" "
            />
            
        </div>
    )
}

export default Imagehelper;
